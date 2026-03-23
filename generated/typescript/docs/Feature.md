
# Feature


## Properties

Name | Type
------------ | -------------
`geometry` | [FeatureGeometry](FeatureGeometry.md)
`properties` | [FeatureProperties](FeatureProperties.md)
`type` | string

## Example

```typescript
import type { Feature } from '@naurt/api'

// TODO: Update the object below with actual values
const example = {
  "geometry": null,
  "properties": null,
  "type": null,
} satisfies Feature

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as Feature
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


