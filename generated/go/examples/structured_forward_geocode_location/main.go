package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"

	naurt "github.com/Naurt-Ltd/api_specification/generated/go"
)

func main() {

	api_key_b, err := os.ReadFile("examples/api.key")

	if err != nil {
		panic(err)
	}

	api_key := string(api_key_b)

	cfg := naurt.NewConfiguration()
	cfg.Servers = naurt.ServerConfigurations{
		{
			URL: "https://api.naurt.net",
		},
	}

	client := naurt.NewAPIClient(cfg)

	ctx := context.WithValue(
		context.Background(),
		naurt.ContextAPIKeys,
		map[string]naurt.APIKey{
			"ApiKeyAuth": {Key: api_key, Prefix: ""}, // MUST be `ApiKeyAuth`, `Prefix: ""` is VERY important
		},
	)

	req := naurt.FinalDestinationRequest{
		Queries: []naurt.FinalDestinationQuery{
			{
				AddressStructured: &naurt.StructuredAddress{
					Postalcode:   naurt.PtrString("10013"),
					StreetName:   naurt.PtrString("Broome Street"),
					StreetNumber: naurt.PtrString("489"),
					City:         naurt.PtrString("New York"),
				},
				Location: &naurt.FinalDestinationLocation{
					Latitude:  40.72,
					Longitude: -73.99,
				},
			},
		},
		Options: nil,
	}

	resp, http, err := client.FinalDestinationAPI.FinaldestinationPost(ctx).FinalDestinationRequest(req).Execute()

	if err != nil {
		fmt.Println(http)
		panic(err)
	}

	fmt.Printf("%+v\n", http)
	fmt.Printf("%+v\n", resp)

	b, err := json.MarshalIndent(resp, "", "  ")
	if err != nil {
		panic(err)
	}

	fmt.Println(string(b))
}
