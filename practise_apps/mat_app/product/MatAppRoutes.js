MatApp.config(['$routeProvider',
        function($routeProvider) {
            $routeProvider.
                when('/', {
                    templateUrl: 'angular-route-template-1.jsp',
                    controller: 'RouteController'
                }).
                when('/product', {
                    templateUrl: 'angular-route-template-2.jsp',
                    controller: 'RouteController'
                }).
                otherwise({
                    redirectTo: '/'
                });
        }]);