const { readFileSync, writeFile } = require('fs');


function cleanProduct(product){
    const {_id, seller, createdAt} = product;

    const fieldsToDelete = [
        'images', 'videos', 'likes', 'views', '__v', 'updatedAt'
    ]

    for(let field of fieldsToDelete){
        delete(product[field])
    }

    return {
        ...product, _id: _id.$oid, seller: seller.$date, createdAt: createdAt.$date 
    }
}

const data = JSON.parse(readFileSync('../raw-data/products.json', {
    encoding: 'utf-8'
})).map(product=>cleanProduct(product));

writeFile('../raw-data/cleanProducts.json', JSON.stringify(data, null, 4), {encoding: 'utf-8'}, (error)=>{
    if(error){
        console.error(error);
    }
})