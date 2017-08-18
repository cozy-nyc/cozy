import React from 'react'
import { Field, reduxForm } from 'redux-form'

const ListingForm = props => {
  const { handleSubmit, pristine, reset, submitting } = props

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label>Price</label>
        <div>
          <Field
            name="Price"
            component="input"
            type="number"
            placeholder="Price"
          />
        </div>
      </div>
      <div>
        <label>CoidtionRating</label>
        <div>
          <Field
            name="ConditionRating"
            component="input"
            type="number"
            placeholder="ConditionRating"
          />
        </div>
      </div>
      <div>
        <label>Size</label>
        <div>
          <Field
            name="size"
            component="input"
            type="number"
            placeholder="Size"
          />
        </div>
      </div>
      <div>
        <label>Description</label>
        <div>
            <Field
              name="description"
              component="textarea"
              placeholder="Type stuff"
            />
        </div>
      </div>
      <div>
        <button type="submit" disabled={pristine || submitting}>
          Submit
        </button>
      </div>
    </form>
  )
}

export default reduxForm({
  form: 'listing' // a unique identifier for this form
})(ListingForm)
