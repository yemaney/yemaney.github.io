package handlers

import (
	"log"
	"net/http"
	"product-api/data"
	"regexp"
	"strconv"
)

// Products is a http.Handler
type Products struct {
	l *log.Logger
}

// NewProducts creates a products handler with the given logger
func NewProducts(l *log.Logger) *Products {
	return &Products{l}
}

// ServeHTTP is the main entry point for the handler and staisfies the http.Handler
// interface
func (p *Products) ServeHTTP(w http.ResponseWriter, r *http.Request) {
	// handle the request for a list of products
	if r.Method == http.MethodGet {
		p.getProducts(w, r)
		return
	}

	if r.Method == http.MethodPost {
		p.addProduct(w, r)
	}

	if r.Method == http.MethodPut {

		re := regexp.MustCompile("/([0-9]+)")
		g := re.FindAllStringSubmatch(r.URL.Path, -1)
		if len(g) != 1 || len(g[0]) != 2 {
			http.Error(w, "Invalid URI", http.StatusBadRequest)
			return
		}

		idString := g[0][1]
		id, err := strconv.Atoi(idString)
		if err != nil {
			http.Error(w, "Invalid URI", http.StatusBadRequest)
			return
		}
		p.l.Printf("Prod: %#v", id)

		p.updateProduct(id, w, r)
		return
	}

	// catch all
	// if no method is satisfied return an error
	w.WriteHeader(http.StatusMethodNotAllowed)
}

// getProducts returns the products from the data store
func (p *Products) getProducts(w http.ResponseWriter, r *http.Request) {
	p.l.Println("Handle GET Products")

	// fetch the products from the datastore
	lp := data.GetProducts()

	// serialize the list to JSON
	err := lp.ToJSON(w)
	if err != nil {
		http.Error(w, "Unable to marshal json", http.StatusInternalServerError)
	}
}

func (p *Products) addProduct(w http.ResponseWriter, r *http.Request) {
	p.l.Println("Handle POST Product")

	prod := &data.Product{}

	err := prod.FromJSON(r.Body)
	if err != nil {
		http.Error(w, "Unable to Unmarshal JSON", http.StatusBadRequest)
	}

	data.AddProduct(prod)
}

func (p *Products) updateProduct(id int, w http.ResponseWriter, r *http.Request) {
	p.l.Println("Handle PUT Product")

	prod := &data.Product{}

	err := prod.FromJSON(r.Body)
	if err != nil {
		http.Error(w, "Unable to Unmarshal JSON", http.StatusBadRequest)
	}

	p.l.Printf("Prod: %#v", prod)
	e := data.UpdateProduct(id, prod)
	if e == data.ErrorProductNotFound {
		http.Error(w, "Product Not Found", http.StatusNotFound)
		return
	}
	if e != nil {
		http.Error(w, "Product Not Found", http.StatusInternalServerError)
		return
	}

}
