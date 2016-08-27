articlesapp.controller("PaginationController", ["$scope", "$location", "$anchorScroll", function ($scope, $location, $anchorScroll) {
    $scope.pageChangeHandler = function (num) {
        console.log('page changed to ' + num);
        $(window).scroll(function () {
            if ($(this).scrollTop() > 100) {
                $('.scrollup').fadeIn();
            } else {
                $('.scrollup').fadeOut();
            }
        });
        $("html, body").animate({
                scrollTop: 0
            }, 600);
    };
}]);