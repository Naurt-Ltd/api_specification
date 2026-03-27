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

	req := naurt.FinalDestinationRequest{
		Queries: []naurt.FinalDestinationQuery{
			{
				AddressString: naurt.PtrString("47 Digby Rd, Evesham WR11 1BW"),
			},
		},
		Options: nil,
	}

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
