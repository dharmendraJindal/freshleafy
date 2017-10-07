JSApps.controller('ProductController', ["$scope", "$rootScope", "$http", function ($scope, $rootScope, $http) {

    getProducts();

    $scope.addProduct = function addProduct(product, rateOfSelectedPackSize) {
        console.log(product);
        product.totalQuantity += 1;
        $rootScope.cartHandler.addProduct(product, rateOfSelectedPackSize, product.totalQuantity)
    };

//function getProducts() {
//    $http.get("http://lit-dusk-68336.herokuapp.com/api/v1/product/products/")
//    .then(
//    function (response){
//
//    console.log(response.data);
//    $scope.products=response.data;
//
//    },
//    function (error){}
//    );
//
//
//}

    function getProducts() {
        $scope.products = [
            {
                "name": "Kakdi",
                "hindi_name": "Kakdi",
                "image_path": "/static/product_images/cucumber_kakdi_500.jpg",
                "product_category": [
                    {
                        "name": "Vegetables"
                    }
                ],
                "grade": "A",
                "rate": "30",
                "unit": "Kg",
                "product_id": 1,
                "totalQuantity": 0,
                "rateOfSelectedPackSize": 30,
                "quantity_intervals": {
                    "pack_size_rates": [
                        30,
                        60,
                        100,
                        150,
                        200
                    ],
                    "pack_size_types": [
                        "100 gm",
                        "200 gm",
                        "500 gm",
                        "1 Kg",
                        "5 Kg"
                    ]
                }
            },
            {
                "name": "Guava",
                "hindi_name": "Guava",
                "image_path": "/static/product_images/guava_peru_500_gm.jpg",
                "product_category": [
                    {
                        "name": "Vegetables"
                    }
                ],
                "grade": "A",
                "rate": "80",
                "unit": "Kg",
                "product_id": 2,
                "totalQuantity": 0,
                "rateOfSelectedPackSize": 30,
                "quantity_intervals": {
                    "pack_size_rates": [
                        30,
                        60,
                        100,
                        150,
                        200
                    ],
                    "pack_size_types": [
                        "100 gm",
                        "200 gm",
                        "500 gm",
                        "1 Kg",
                        "5 Kg"
                    ]
                }
            },
            {
                "name": "Tomato",
                "hindi_name": "Tomato",
                "image_path": "/static/product_images/cherry_tomato_250_gm.jpg",
                "product_category": [
                    {
                        "name": "Fruits"
                    },
                    {
                        "name": "Vegetables"
                    }
                ],
                "grade": "A",
                "rate": "150",
                "unit": "Kg",
                "product_id": 3,
                "totalQuantity": 0,
                "rateOfSelectedPackSize": 30,
                "quantity_intervals": {
                    "pack_size_rates": [
                        30,
                        60,
                        100,
                        150,
                        200
                    ],
                    "pack_size_types": [
                        "100 gm",
                        "200 gm",
                        "500 gm",
                        "1 Kg",
                        "5 Kg"
                    ]
                }
            },
            {
                "name": "Dhaniya",
                "hindi_name": "Dhaniya",
                "image_path": "/static/product_images/coriander_dhania.jpg",
                "product_category": [
                    {
                        "name": "Fruits"
                    }
                ],
                "grade": "A",
                "rate": "50",
                "unit": "Kg",
                "product_id": 4,
                "totalQuantity": 0,
                "rateOfSelectedPackSize": 30,
                "quantity_intervals": {
                    "pack_size_rates": [
                        30,
                        60,
                        100,
                        150,
                        200
                    ],
                    "pack_size_types": [
                        "100 gm",
                        "200 gm",
                        "500 gm",
                        "1 Kg",
                        "5 Kg"
                    ]
                }
            },
            {
                "name": "Mango1",
                "hindi_name": "Mango1",
                "image_path": "/static/product_images/mango_totapuri.jpg",
                "product_category": [
                    {
                        "name": "Fruits"
                    }
                ],
                "grade": "A",
                "rate": "250",
                "unit": "Kg",
                "product_id": 5,
                "totalQuantity": 0,
                "rateOfSelectedPackSize": 30,
                "quantity_intervals": {
                    "pack_size_rates": [
                        30,
                        60,
                        100,
                        150,
                        200
                    ],
                    "pack_size_types": [
                        "100 gm",
                        "200 gm",
                        "500 gm",
                        "1 Kg",
                        "5 Kg"
                    ]
                }
            }
        ]
    }


    $scope.getFullImageUrl = function getFullImageUrl(imagePath) {
        return "http://lit-dusk-68336.herokuapp.com" + imagePath;
    }

}]);