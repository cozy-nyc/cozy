export const selectCategory = (category) => {
   console.log("You clicked on category: ", category.name);
   return {
      type: "CATEGORY_SELECTED",
      payload: category
   }
};
