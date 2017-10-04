MatApp.config(['$routeProvider',
        function($routeProvider) {
            $routeProvider.
                when('/', {
                    templateUrl: 'index.html',
                    controller: 'HomeController.js'
                }).
                when('/products', {
                    templateUrl: 'product/ProductContent.html',
                    controller: 'ProductController'
                }).
                otherwise({
                    redirectTo: '/'
                });
        }]);