use std::{fs, str::FromStr};

use naurt_api::{
    apis::{
        configuration::{ApiKey, Configuration},
        final_destination_api::finaldestination_post,
    },
    models::{FinalDestinationLocation, FinalDestinationQuery, FinalDestinationRequest},
};
use reqwest::Client;
use uuid::Uuid;

#[tokio::main]
async fn main() {
    let api_key = fs::read_to_string("api.key").unwrap();

    let req = FinalDestinationRequest {
        queries: vec![
            FinalDestinationQuery {
                id: Some(Uuid::from_str("c56dbebb-c7ab-ede2-a7ac-f84e57d1878d").unwrap()),
                ..Default::default()
            },
            FinalDestinationQuery {
                address_string: Some("47 Digby Rd, Evesham WR11 1BW".to_string()),
                ..Default::default()
            },
            FinalDestinationQuery {
                location: Some(Box::new(FinalDestinationLocation {
                    latitude: 47.364,
                    longitude: 1.722,
                    distance_filter: None,
                })),
                additional_matches: Some(true),
                ..Default::default()
            },
        ],
        options: None,
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
