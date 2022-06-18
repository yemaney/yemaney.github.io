package banking

import (
	"errors"
	"fmt"
)

// custom type for bitcoin
type Bitcoin int

// implementing Stringer interface for Bitcoin
func (b Bitcoin) String() string {
	return fmt.Sprintf("%d BTC", b)
}

// struct representing a wallet
type Wallet struct {
	balance Bitcoin
}

// add a Bitcoin to the wallets current balance
func (w *Wallet) Deposit(d Bitcoin) {
	w.balance += d
}

// returns the current Bitcoin balance of the wallet
func (w *Wallet) Balance() Bitcoin {
	return w.balance
}

// custom error for insufficient funds
var ErrInsufficientFunds = errors.New("cannot withdraw, insufficient funds")

// reduce current Bitcoin balance
func (w *Wallet) Withdraw(amount Bitcoin) error {
	if amount > w.balance {
		return ErrInsufficientFunds
	}

	w.balance -= amount
	return nil
}
