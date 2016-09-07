productapp.controller("OrderSummaryController", ["$scope", "$routeParams", "$location", "OrderSummaryService",
    function ($scope, $routeParams, $location, OrderSummaryService) {

        var getOrders = function () {
            OrderSummaryService.getOrderSummary().then(function (data) {
                console.log(data);
                $scope.order = data[0];
            }, function () {

            });
        };
        getOrders();


    }]);
