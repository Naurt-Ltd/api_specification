use std::fs;

use naurt_api::{
    apis::{
        configuration::{ApiKey, Configuration},
        final_destination_api::finaldestination_post,
    },
    models::{
        FinalDestinationOptions, FinalDestinationQuery, FinalDestinationRequest, StructuredAddress,
    },
};
use reqwest::Client;

#[tokio::main]
async fn main() {
    let api_key = fs::read_to_string("api.key").unwrap();

    let req = FinalDestinationRequest {
        queries: vec![FinalDestinationQuery {
            address_structured: Some(Box::new(StructuredAddress {
                postalcode: Some("10013".to_string()),
                street_name: Some("Broome Street".to_string()),
                street_number: Some("489".to_string()),
                city: Some("New York".to_string()),
                ..Default::default()
            })),
            ..Default::default()
        }],
        options: Some(Box::new(FinalDestinationOptions {
            pretty_print: Some(true),
            ..Default::default()
        })),
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
