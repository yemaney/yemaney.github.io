package concurrency

import "net/http"

// abstract a Website check to help with tests
type WebsiteChecker func(string) bool

// data type for go channel
type result struct {
	string
	bool
}

// returns true if url response is 200 else false
func CheckWebsite(url string) bool {
	response, err := http.Head(url)
	if err != nil {
		return false
	}

	return response.StatusCode == http.StatusOK
}

// call check website for multiple urls
// use go routines to enable concurrency
// use channels to make sure the result is done in order
func CheckWebsites(wc WebsiteChecker, urls []string) map[string]bool {
	results := make(map[string]bool)
	resultChannel := make(chan result)

	for _, url := range urls {
		go func(u string) {
			resultChannel <- result{u, wc(u)}
		}(url)
	}

	for i := 0; i < len(urls); i++ {
		r := <-resultChannel
		results[r.string] = r.bool
	}
	return results
}
