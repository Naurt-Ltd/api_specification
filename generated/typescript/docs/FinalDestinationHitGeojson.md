
# FinalDestinationHitGeojson


## Properties

Name | Type
------------ | -------------
`features` | [Array&lt;Feature&gt;](Feature.md)
`type` | string
`building` | [Polygon](Polygon.md)
`defaultGeocode` | [Point](Point.md)
`entrance` | [Multipoint](Multipoint.md)
`parking` | [Polygon](Polygon.md)

## Example

```typescript
import type { FinalDestinationHitGeojson } from '@naurt/api'

// TODO: Update the object below with actual values
const example = {
  "features": null,
  "type": null,
  "building": null,
  "defaultGeocode": null,
  "entrance": null,
  "parking": null,
} satisfies FinalDestinationHitGeojson

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as FinalDestinationHitGeojson
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


