package main

import "fmt"

type IGun interface {
	getPower() int
	getName() string
	setPower(power int)
	setName(name string)
}

type gun struct {
	power int
	name  string
}

func (g *gun) setName(name string) {
	g.name = name
}

func (g *gun) getName() string {
	return g.name
}

func (g *gun) setPower(power int) {
	g.power = power
}

func (g *gun) getPower() int {
	return g.power
}

// AK47
type AK47 struct {
	gun
}

func newAK47() IGun {
	return &AK47{
		gun: gun{
			name:  "AK47",
			power: 100,
		},
	}
}

// Pistol
type Pistol struct {
	gun
}

func newPistol() IGun {
	return &Pistol{
		gun: gun{
			name:  "Pistol",
			power: 10,
		},
	}
}

func makeGun(gunType string) (IGun, error) {
	if gunType == "ak47" {
		return newAK47(), nil
	}
	if gunType == "pistol" {
		return newPistol(), nil
	}
	return nil, fmt.Errorf("Wrong gun type passed")
}

func main() {
	ak47, _ := makeGun("ak47")
	pistol, _ := makeGun("pistol")

	fmt.Println(ak47.getName())
	fmt.Println(pistol.getName())
}
