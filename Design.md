Object:

  - GET-able or not: lazy on attribute reading
  - PATCH-able or not: object.edit( ... )
  - DELETE-able or not: object.delete()
  - has attributes
    - scalars (in the GET for the object)
    - lists (in a specific GET)

Scalar:

  - fondamental type or objet

List:

  - contains fondamental type or objet
  - GET-able or not
  - elements GET-able or not
    - to ask if an element is in the list
  - elements PUT-able or not
    - add an existing element to the list: parent.add_to_elements( element )
  - POST-able or not
    - create a new element and add it to the list: parent.create_element( ... )
  - elements DELETE-able or not
    - delete an element from a list can have two meanings:
      - the element's life is finished: element.delete()
      - the element is just removed from the list, but continues to live somewhere else: parent.remove_from_elements( element )
