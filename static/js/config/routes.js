productapp.config(["$routeProvider", "$resourceProvider", "$locationProvider",
    function ($routeProvider, $resourceProvider, $locationProvider) {
        $resourceProvider.defaults.stripTrailingSlashes = false;
        $routeProvider
            .when("/", {
                templateUrl: "/static/js/product/partials/ListOfAllArticles.html",
                controller: "ListOfAllProductCategoryController"
            })
            .when("/login", {
                controller: "LoginController",
                templateUrl: "/static/partials/authentication/login.html"
            })
            .when("/register", {
                controller: "RegisterController",
                templateUrl: "/static/partials/authentication/register.html"
            })
            .otherwise({
                redirectTo: '/'
            });

        $locationProvider.html5Mode(true);
    }
]);