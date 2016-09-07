productapp.controller("OrderSummaryController", ["$scope", "$routeParams", "$location", "UserOrderService",
    function ($scope, $routeParams, $location, UserOrderService) {

        var getTotalOrders = function () {
            UserOrderService.getUserOrders().then(function (data) {
                $scope.orderedProducts = data;
            }, function () {

            });
        };
        
        getTotalOrders();

    }]);
