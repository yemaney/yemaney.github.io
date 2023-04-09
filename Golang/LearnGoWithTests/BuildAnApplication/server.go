package main

import (
	"fmt"
	"net/http"
	"strings"
)

// A PlayStore is where data is persisted for the game server
// GetPlayerScore : takes a players name and returns the players current number of wins
// REcordWin : takes a players name and increments the number of wins for them by 1
type PlayerStore interface {
	GetPlayerScore(name string) int
	RecordWin(name string)
}

// The game server. Will receive requests and interact with the PlayStore to retrieve data
type PlayerServer struct {
	store PlayerStore
}

// Implementation of the `http.ListenAndServe` interface. Acts as the server and routes
// requests to the correct helper functions.
func (p *PlayerServer) ServeHTTP(w http.ResponseWriter, r *http.Request) {
	player := strings.TrimPrefix(r.URL.Path, "/players/")

	switch r.Method {
	case http.MethodPost:
		p.processWin(w, player)
	case http.MethodGet:
		p.showScore(w, player)
	}

}

// The GET endpoint of the server. Takes a players  name and calls the servers
// PlayStore.GetPlayerScore with it. If the person doesn't exist in the PlayStore
// the status code of the returned response should be http.StatusNotFound (404)
func (p *PlayerServer) showScore(w http.ResponseWriter, player string) {
	score := p.store.GetPlayerScore(player)

	if score == 0 {
		w.WriteHeader(http.StatusNotFound)
	}

	fmt.Fprint(w, score)
}

// The POST endpoint of the server. Takes a players name and calls the servers
// PlayStore.RecordWin with it. Intended to record that a player has won a new game.
func (p *PlayerServer) processWin(w http.ResponseWriter, player string) {
	p.store.RecordWin(player)
	w.WriteHeader(http.StatusAccepted)
}
