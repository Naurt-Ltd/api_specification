
# FinalDestinationLocation

A location, using WGS84 latitude and longitude.  Used for a reverse geocode, or to add some location bias to a forward geocode.  Use `distance_filter` to optionally limit the distance from this point that  results can appear within 

## Properties

Name | Type
------------ | -------------
`latitude` | number
`longitude` | number
`distanceFilter` | number

## Example

```typescript
import type { FinalDestinationLocation } from '@naurt/api'

// TODO: Update the object below with actual values
const example = {
  "latitude": null,
  "longitude": null,
  "distanceFilter": null,
} satisfies FinalDestinationLocation

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as FinalDestinationLocation
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


