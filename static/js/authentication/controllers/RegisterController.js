productapp.controller("RegisterController", ["$location", "$scope", "Authentication",
    function ($location, $scope, Authentication) {
        var account = {
            firstName:"",
            lastName:"",
            email: "",
            password: "",
            confirmPassword:"",
            phone_number : "",
            companyName:""
        };
        $scope.account=angular.copy(account);
        $scope.register = register;

        function register() {
        if($scope.RegisterForm.$invalid){
        return false;
        }
            Authentication.register($scope.account).then(function(){
            $location.path('/login');
            },function(){
            });
        }
    }]);