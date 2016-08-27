productsapp.config(["$routeProvider", "$resourceProvider", "$locationProvider",
    function ($routeProvider, $resourceProvider, $locationProvider) {
        $resourceProvider.defaults.stripTrailingSlashes = false;
        $routeProvider
            .when("/", {
                templateUrl: "/static/partials/articles/ListOfAllArticles.html",
                controller: "ListOfAllArticleController"
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