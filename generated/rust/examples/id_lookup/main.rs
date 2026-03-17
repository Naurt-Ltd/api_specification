use std::{fs, str::FromStr};

use naurt_api::{
    apis::{
        configuration::{ApiKey, Configuration},
        final_destination_api::finaldestination_post,
    },
    models::{FinalDestinationOptions, FinalDestinationQuery, FinalDestinationRequest},
};
use reqwest::Client;
use uuid::Uuid;

#[tokio::main]
async fn main() {
    let api_key = fs::read_to_string("api.key").unwrap();

    let req = FinalDestinationRequest {
        queries: vec![FinalDestinationQuery {
            id: Some(Uuid::from_str("8bd197aa-7328-3e10-9ea7-7ec139e9fa48").unwrap()),
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
