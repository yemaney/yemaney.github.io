package poker_test

import (
	"strings"
	"testing"

	poker "gameserver"
)

func TestCLI(t *testing.T) {

	t.Run("record chris win from user input", func(t *testing.T) {
		in := strings.NewReader("Chris wins\n")
		playerStore := &poker.StubPlayerStore{}

		game := poker.NewCLI(playerStore, in)
		game.PlayPoker()

		poker.AssertPlayerWin(t, playerStore, "Chris")
	})

	t.Run("record cleo win from user input", func(t *testing.T) {
		in := strings.NewReader("Cleo wins\n")
		playerStore := &poker.StubPlayerStore{}

		game := poker.NewCLI(playerStore, in)
		game.PlayPoker()

		poker.AssertPlayerWin(t, playerStore, "Cleo")
	})

}
