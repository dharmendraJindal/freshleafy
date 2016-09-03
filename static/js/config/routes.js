productapp.config(["$routeProvider", "$resourceProvider", "$locationProvider",
    function ($routeProvider, $resourceProvider, $locationProvider) {
        $resourceProvider.defaults.stripTrailingSlashes = false;
        $routeProvider
            .when("/", {
                templateUrl: "/static/js/product/partials/ListOfAllProductCategories.html",
                controller: "ListOfAllProductCategoryController"
            })
            .when("/login", {
                controller: "LoginController",
                templateUrl: "/static/js/authentication/partials/login.html"
            })
            .when("/register", {
                controller: "RegisterController",
                templateUrl: "/static/js/authentication/partials/register.html"
            })
            .otherwise({
                redirectTo: '/'
            });

        $locationProvider.html5Mode(true);
    }
]);