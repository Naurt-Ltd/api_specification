
# StructuredAddress

Naurt\'s own format for structured address data. Please see:  https://docs.naurt.com/reference/address-structure/ for significant more  details on this data format.  When searching, do not use `country_code` - as it is not used. `country_code` is for responses only. 

## Properties

Name | Type
------------ | -------------
`unit` | string
`houseName` | string
`streetNumber` | string
`streetName` | string
`locality` | string
`city` | string
`county` | string
`state` | string
`country` | string
`postalcode` | string
`countryCode` | [Country](Country.md)

## Example

```typescript
import type { StructuredAddress } from '@naurt/api'

// TODO: Update the object below with actual values
const example = {
  "unit": null,
  "houseName": null,
  "streetNumber": null,
  "streetName": null,
  "locality": null,
  "city": null,
  "county": null,
  "state": null,
  "country": null,
  "postalcode": null,
  "countryCode": null,
} satisfies StructuredAddress

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as StructuredAddress
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


