productapp.config(["$routeProvider", "$resourceProvider", "$locationProvider",
    function ($routeProvider, $resourceProvider, $locationProvider) {
        console.log('in routes');
        $resourceProvider.defaults.stripTrailingSlashes = false;

        $routeProvider
            .when("/home", {
                controller: "ListOfAllProductCategoryController",
                templateUrl: "/static/js/product/partials/ListOfAllProductCategories.html"
            }

            )
            .when("/home/login", {
                controller: "LoginController",
                templateUrl: "/static/js/authentication/partials/login.html"
            })
            .when("/home/register", {
                controller: "RegisterController",
                templateUrl: "/static/js/authentication/partials/register.html"
            })
            
            .when("/home/vieworders", {
                controller: "OrderSummaryController",
                templateUrl: "/static/js/product/partials/OrderSummary.html"
            })
            
            .when("/home/testngcart", {
                controller: "TestNGCartController",
                templateUrl: "/static/js/product/partials/TestNGCart.html"
            })
            .otherwise({
                redirectTo: '/home'
            });

        $locationProvider.html5Mode(true);
    }
]);