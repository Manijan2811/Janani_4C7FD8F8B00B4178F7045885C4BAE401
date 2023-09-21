#write a function called linear_search_product that takes the list of products and a target_product name as input,the function should perform a linear search to find the target product in the list and return a list of indices of all occurences of the product if found or an empty list if the product is not found


def linear_search_product(product_list,target_product):
  indices=[]
  for index,product in enumerate(product_list):
    if product==target_product:
      indices.append(index)
  return indices
products=["Computer","CPU","Mouse","Keyboard","Computer","Mouse"]
target="Computer"
target1="Pendrive"
result=linear_search_product(products,target)
result1=linear_search_product(products,target1)
print(result)
print(result1)
