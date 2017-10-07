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

              .when('/cartcheckout', {
                    templateUrl: '/static/JSApps/cart/CartCheckout.html',
                    controller: 'CartCheckoutController'
                })
            .otherwise({
                redirectTo: '/'
            });
    }
]);