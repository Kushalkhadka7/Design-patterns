package main

import "fmt"

type IDatbase interface {
	getUsers() string
}

type Database struct{}

var cache map[string]string

func newDatabase() IDatbase {
	return &Database{}
}

func (d *Database) getUsers() string {
	return "Users from database"
}

type CachedDb struct {
	db IDatbase
}

func newCachedDB(db IDatbase) IDatbase {
	return &CachedDb{
		db: newDatabase(),
	}
}

func (cd *CachedDb) getUsers() string {
	data, ok := cache["users"]
	if ok {
		return data
	}

	cache["users"] = "users"
	return "Found uses on cache"

}

type DBManager struct{}

func newDBManager() IDatbase {
	return &DBManager{}
}

func (dbm DBManager) getUsers() string {
	d := newDatabase()
	c := newCachedDB(d)

	return c.getUsers()
}

func main() {
	db := newDBManager()
	fmt.Println(db.getUsers())
	fmt.Println(db.getUsers())
}
