
# Language

Used for reverse geocodes only, to decide which language the response is in.  In a forward geocode, the response language will match the input language.  See: https://docs.naurt.com/reference/language/ for detailed information on  language availability for all countries (not all countries have alternative  languages) 

## Properties

Name | Type
------------ | -------------

## Example

```typescript
import type { Language } from '@naurt/api'

// TODO: Update the object below with actual values
const example = {
} satisfies Language

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as Language
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


