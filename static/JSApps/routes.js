JSApps.config(["$routeProvider",
    function ($routeProvider) {
        $routeProvider
              .when('/', {
                    templateUrl: '/static/JSApps/home/Home.html',
                    controller: 'HomeController'
                })
                .when('/products', {
                    templateUrl: '/static/JSApps/product/ProductContent.html',
                    controller: 'ProductController'
                })
            .otherwise({
                redirectTo: '/'
            });
    }
]);