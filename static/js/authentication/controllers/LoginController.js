productapp.controller("LoginController", ["$location", "$scope", "Authentication",
    function ($location, $scope, Authentication) {

        var account = {
            username: "",
            password: ""
        };
        $scope.account=angular.copy(account);
        $scope.login = login;
        activate();
        function activate() {
            if (Authentication.isAuthenticated()) {
                $location.url("/home");
            }
        }

        function login() {
            if($scope.LoginForm.$invalid) {
            return false;
            }
            Authentication.login($scope.account).then(function(){
            $scope.inValidCredentials=false;
            },function(){
            $scope.inValidCredentials=true;
            });
        }
    }]);