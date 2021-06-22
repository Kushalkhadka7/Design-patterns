package main

import "fmt"

type IConverter interface {
	convertVideo()
}

type VideoConverter struct {
	fileName string
}

func newConverter(fileName string) IConverter {
	return &VideoConverter{
		fileName: fileName,
	}
}

func (vc *VideoConverter) convertVideo() {
	newProcessor(vc.fileName).processVideo()
	newCompressor(vc.fileName).compressVideo()

	fmt.Println("Converting video file")
}

type Processor struct {
	fileName string
}

type IProcessor interface {
	processVideo()
}

// Process video
func newProcessor(fileName string) IProcessor {
	return &Processor{
		fileName: fileName,
	}
}

func (p *Processor) processVideo() {
	fmt.Println("Processing video file")
}

type Compressor struct {
	fileName string
}

type ICompressor interface {
	compressVideo()
}

// Compress video
func newCompressor(fileName string) ICompressor {
	return &Compressor{
		fileName: fileName,
	}
}

func (p *Compressor) compressVideo() {
	fmt.Println("Compressing video file")
}

func main() {
	videoConvert := newConverter("video.mp4")
	videoConvert.convertVideo()
}
