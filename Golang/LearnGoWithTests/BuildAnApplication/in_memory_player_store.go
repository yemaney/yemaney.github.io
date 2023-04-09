package main

// initializer that creates and returns a new *InMemoryPlayerStore
func NewInMemoryPlayerStore() *InMemoryPlayerStore {
	return &InMemoryPlayerStore{map[string]int{}}
}

// acts as datastore for game server
// sore : key value store containing (name, score) pairs
type InMemoryPlayerStore struct {
	store map[string]int
}

// increment number of wins for a player
func (i *InMemoryPlayerStore) RecordWin(name string) {
	i.store[name]++
}

// get a players current number of wins
func (i *InMemoryPlayerStore) GetPlayerScore(name string) int {
	return i.store[name]
}

func (i *InMemoryPlayerStore) GetLeague() []Player {
	var league []Player
	for name, wins := range i.store {
		league = append(league, Player{name, wins})
	}
	return league
}
