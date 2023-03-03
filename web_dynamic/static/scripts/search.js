const searchBtn = document.getElementById('search')
const locationSearch = document.getElementById('location')
const resourceType = document.getElementById('resource')
const resultTitle = document.getElementById('result-title')
const resultBody = document.getElementById('result-body')


searchBtn.addEventListener('click', () => {
    fetch('http://127.0.0.1:5000/search', {
        body: JSON.stringify({
            resource: resourceType.value,
            location: locationSearch.value
        }),
        method: 'POST'
    })
    .then((res) => {
        if (!res.ok) {
            throw new Error('Network has issues')
        }
        return res.json()
    })
    .then((data) => {
        console.log(data)
        console.log(data.heading)
        resultBody.innerHTML = ""
        resultTitle.innerText = data.heading
        for (const result of data.data){
            if (data.total_rate === 0) {
                data.total_rate = "Not rated"
            }
            if (data.resource_type === "restaurant") {
        resultBody.insertAdjacentHTML('beforeend', `<article class="col-3 mb-3 d-flex justify-content-between">
        <div class="card" style="width: 18rem;">
          <img src="static/images/background/bg-1.jpeg" class="card-img-top" alt="...">
          <div class="card-body">
            <h5 class="card-title">${result.name}</h5>
            <p class="card-text fst-italic description" style="font-size: 13px;">${result.description}</p> 
        </div>
        <ul class="list-group list-group-flush">
          <li class="list-group-item">Price Range: <span class="float-end">&#8358;${ result.min } - &#8358;${ result.max }</span></li>
          <li class="list-group-item">Location: <span class="float-end">${ result.address }, ${ result.city } </span></li>
          <li class="list-group-item">Rating: <span class="float-end">${ result.total_rate }</span></li>
          <li class="list-group-item">No. of Reviews <span class="float-end">${ result.no_of_reviews }</span></li>
        </ul>
        <div class="card-body">
          <a href="/restaurants/${ result.id }" class="card-link"><button class="btn btn-sm btn-outline-primary">See more</button></a>
          <a href="/restaurants/review/${ result.id }" class="card-link"><button class="btn btn-sm btn-outline-primary float-end">Review</button></a>
        </div> 
    </article>`)
            }
            else if (data.resource_type === "food") {
                resultBody.insertAdjacentHTML('beforeend', `<article class="col-3 mb-3 d-flex justify-content-between">
                <div class="card" style="width: 18rem;">
                  <img src="static/images/background/bg-1.jpeg" class="card-img-top" alt="...">
                  <div class="card-body">
                    <h5 class="card-title">${ result.name }</h5>
                    <p class="card-text fst-italic description" style="font-size: 13px;">${ result.description }</p> 
                </div>
                <ul class="list-group list-group-flush">
                  <li class="list-group-item">Served By <span class="float-end"><a href="/restaurants/${ result.restaurant_id }">${ result.restaurant_name }</a></span></li>
                  <li class="list-group-item">Price <span class="float-end">&#8358;${ result.price }</span></li>
                  <li class="list-group-item">Rating: <span class="float-end">${ result.total_rate }</span></li>
                  <li class="list-group-item">No. of Reviews <span class="float-end">${ result.no_of_reviews }</span></li>
                </ul>
                <div class="card-body">
                  <a href="/foods/${ result.id }" class="card-link"><button class="btn btn-sm btn-outline-primary">See more</button></a>
                  <a href="/foods/review/${ result.id }" class="card-link"><button class="btn btn-sm btn-outline-primary float-end">Review</button></a>
                </div>
            </article>`)
            }
    }

    })
    .catch((err) => {
        console.log('there was an error', err)
    })
})
