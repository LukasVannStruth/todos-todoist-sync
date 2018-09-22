extern crate hyper;

use hyper::Client;
use hyper::rt::{self, Future, Stream};
use http::{Request, Response};

fn main() {
    //TODO: print out api response from todoist.
    rt::run(test_get());
    
}

fn test_get() -> impl Future<Item=(), Error=()> {
    let client = Client::new();

    let uri = "http://httpbin.org/ip".parse().unwrap();

    client
        .get(uri)
        .map(|res| {
            println!("Response: {}", res.status());
        })
        .map_err(|err| {
            println!("Error: {}", err);
        })
}
