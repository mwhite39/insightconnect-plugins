package actions

// Code generated by the Komand Go SDK Generator. DO NOT EDIT

// Md5ExtractorInput is the input for Md5Extractor
type Md5ExtractorInput struct {
	File []byte `json:"file"`
	Str  string `json:"str"`
}

// Md5ExtractorOutput is the output for Md5Extractor
type Md5ExtractorOutput struct {
	Md5 []string `json:"md5"`
}

// Md5ExtractorAction is an action the plugin can take
type Md5ExtractorAction struct{}