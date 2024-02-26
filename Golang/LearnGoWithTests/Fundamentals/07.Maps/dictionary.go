package main

// custom type for a dictionary
type Dictionary map[string]string

// custom type for dictionary errors
type DictionaryErr string

// implementing the error interface on DictionaryErr
func (e DictionaryErr) Error() string {
	return string(e)
}

const (
	// custom error for keys not found in dictionary
	ErrNotFound = DictionaryErr("could not find the word you were looking for")
	// custom error when trying to add a key that already exists
	ErrWordExists = DictionaryErr("cannot add word because it already exists")
	// custom error when trying to update a key that doesn't exist
	ErrWordDoesNotExist = DictionaryErr("cannot update word because it does not exist")
)

// method to search dictionary
func (d Dictionary) Search(word string) (string, error) {
	definition, ok := d[word]

	if !ok {
		return "", ErrNotFound
	}

	return definition, nil
}

// method to add a key-value pair to dictionary
func (d Dictionary) Add(word, definition string) error {
	_, err := d.Search(word)

	switch err {
	case ErrNotFound:
		d[word] = definition
	case nil:
		return ErrWordExists
	default:
		return err
	}
	return nil
}

// method to update word definition in dictionary
func (d Dictionary) Update(word, definition string) error {
	_, err := d.Search(word)

	switch err {
	case ErrNotFound:
		return ErrWordDoesNotExist
	case nil:
		d[word] = definition
	default:
		return err
	}

	return nil
}

// method to delete a word from a dictionary
func (d Dictionary) Delete(word string) {
	delete(d, word)
}
