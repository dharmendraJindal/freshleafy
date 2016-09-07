productapp.config(["$routeProvider", "$resourceProvider", "$locationProvider",
    function ($routeProvider, $resourceProvider, $locationProvider) {
        $resourceProvider.defaults.stripTrailingSlashes = false;
        $routeProvider
            .when("/", {
                controller: "ListOfAllProductCategoryController",
                templateUrl: "/static/js/product/partials/ListOfAllProductCategories.html"
            })
            .when("/login", {
                controller: "LoginController",
                templateUrl: "/static/js/authentication/partials/login.html"
            })
            .when("/register", {
                controller: "RegisterController",
                templateUrl: "/static/js/authentication/partials/register.html"
            })
            
            .when("/vieworders", {
                controller: "OrderSummaryController",
                templateUrl: "/static/js/product/partials/OrderSummary.html"
            })
            
            .when("/testngcart", {
                controller: "TestNGCartController",
                templateUrl: "/static/js/product/partials/TestNGCart.html"
            })
            .otherwise({
                redirectTo: '/'
            });

        $locationProvider.html5Mode(true);
    }
]);