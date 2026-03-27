use std::fs;

use naurt_api::{
    apis::{
        configuration::{ApiKey, Configuration},
        final_destination_api::finaldestination_post,
    },
    models::{
        FinalDestinationLocation, FinalDestinationOptions, FinalDestinationQuery,
        FinalDestinationRequest,
    },
};
use reqwest::Client;

#[tokio::main]
async fn main() {
    let api_key = fs::read_to_string("api.key").unwrap();

    let req = FinalDestinationRequest {
        queries: vec![FinalDestinationQuery {
            address_string: Some("47 Digby Rd, Evesham WR11 1BW".to_string()),
            location: Some(Box::new(FinalDestinationLocation {
                latitude: 52.08,
                longitude: -1.93,
                distance_filter: None,
            })),
            ..Default::default()
        }],
        options: None
    };

    let client = Client::new();

    let api_key = ApiKey {
        key: api_key,
        prefix: None,
    };

    let config = Configuration {
        api_key: Some(api_key),
        base_path: "https://api.naurt.net".to_string(),
        client: client,
        ..Default::default()
    };

    let resp = finaldestination_post(&config, req).await.unwrap();

    println!("{:?}", resp);
}
