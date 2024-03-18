
document.addEventListener("DOMContentLoaded",function(){



const BASE_URL = "http://127.0.0.1:5000/api";

function cupcakeHtml(cupcake){
    
    return `
    <div class="single-cupcake-cont" data-id="${cupcake.id}">
       <h5>${cupcake.flavor}</h5>
       <p>${cupcake.size}</p>
       <p>${cupcake.rating}</p>
       <img class="cupcake-img" src="${cupcake.image}">image</img>
       <button class="delete-btn">Delete</button>
    </div>
    `
}

async function showExistingCupcakes(){
    //for cupcakes list route//
    try{
        const resp = await axios.get(`${BASE_URL}/cupcakes`)
        const cupcakeData = resp.data.cupcakes;
        const cupcakeContainer = $(".cupcake-list")
        cupcakeData.forEach(function(cupcakeData){
            const newCupcake = $(cupcakeHtml(cupcakeData))
            cupcakeContainer.append(newCupcake)
        })
    }catch(error){
      console.error("issue with list of cupcakes",error)
    }

}

$(document).ready(function(){
    showExistingCupcakes()
    
})

$(document).on('submit','.add-cupcake-form',async function(event){
   event.preventDefault();
   const flavor = $('.flavor-field').val()
   const size = $('.size-field').val()
   const rating = $('.rating-field').val()
   const image = $('.image-field').val()

   const resp = await axios.post(`${BASE_URL}/cupcakes`,
   {flavor,size,rating,image})
   const data = resp.data.cupcake;
   const newCupcake = $(cupcakeHtml(data))
   $('.cupcake-list').append(newCupcake)
 //clear input
   $('.flavor-field').val("")
   $('.size-field').val("")
   $('.rating-field').val("")
   $('.image-field').val("")
})



$(document).on('click','.delete-btn',async function(){
    const cupcakeId = $(this).closest(".single-cupcake-cont").attr("data-id")
    $(this).closest(".single-cupcake-cont").remove()
    await axios.delete(`${BASE_URL}/cupcakes/${cupcakeId}`)
    console.log("hey")
})



});