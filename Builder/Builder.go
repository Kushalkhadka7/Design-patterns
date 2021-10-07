package main

import "fmt"

type Product struct {
	wallType  string
	floorType string
	roofType  string
	doorType  string
}

type Builder interface {
	setWallType()
	setFloorType()
	setRoofType()
	setDoorType()
	getHouse() Product
}

func NewBuilder(builderType string) Builder {
	if builderType == "modern" {
		return newModernBuilder()
	} else {
		return newArtBuilder()
	}
}

// Modern builder
type ModernBuilder struct {
	product Product
}

func newModernBuilder() Builder {
	return &ModernBuilder{
		product: Product{},
	}
}

func (b *ModernBuilder) setWallType() {
	b.product.wallType = "Wooden"
}

func (b *ModernBuilder) setDoorType() {
	b.product.doorType = "Wooden Door"
}

func (b *ModernBuilder) setFloorType() {
	b.product.floorType = "marbel"
}

func (b *ModernBuilder) setRoofType() {
	b.product.roofType = "marbel"
}

func (b *ModernBuilder) getHouse() Product {
	return b.product
}

// Art Builder
type ArtBuilder struct {
	product Product
}

func newArtBuilder() Builder {
	return &ArtBuilder{
		product: Product{},
	}
}

func (b *ArtBuilder) setWallType() {
	b.product.wallType = "Stone"
}

func (b *ArtBuilder) setDoorType() {
	b.product.doorType = "Wooden Door"
}

func (b *ArtBuilder) setFloorType() {
	b.product.floorType = "tile"
}

func (b *ArtBuilder) setRoofType() {
	b.product.roofType = "tin"
}

func (b *ArtBuilder) getHouse() Product {
	return b.product
}

// Director

type director struct {
	builder Builder
}

func newDirector(b Builder) *director {
	return &director{
		builder: b,
	}
}

func (d *director) setBuilder(b Builder) {
	d.builder = b
}

func (d *director) buildHouse() Product {
	d.builder.setWallType()
	d.builder.setDoorType()
	d.builder.setFloorType()

	return d.builder.getHouse()
}

func main() {
	modernBuilder := NewBuilder("modern")
	artBuilder := NewBuilder("art")

	fmt.Println(modernBuilder.getHouse())
	fmt.Print(artBuilder.getHouse())

	director := newDirector(modernBuilder)
	director.buildHouse()
}
