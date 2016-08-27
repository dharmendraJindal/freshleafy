productapp.controller("ListOfAllProductCategoryController", ["$scope", "$routeParams", "$location",
    "Authentication", "Articles",
    function ($scope, $rootScope, $location, Authentication, Articles) {
        $scope.currentPage = 1;
        $scope.pageSize = 10;

        $scope.articles = Articles.query();
        $scope.articles.$promise.then(function (result) {
            $scope.product_categories = result;
            console.log(result);
        });
        $scope.show = function (id) {
            $location.url('/article/' + id);
        };
        $scope.edit = function (id) {
            $location.url('/article/edit/' + id);
        };
    }
]);