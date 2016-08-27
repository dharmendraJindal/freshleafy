articlesapp.value('FieldTypes', {
        text: ['Text', 'should be text'],
        email: ['Email', 'should be an email address'],
        number: ['Number', 'should be a number'],
        date: ['Date', 'should be a date'],
        datetime: ['Datetime', 'should be a datetime'],
        time: ['Time', 'should be a time'],
        month: ['Month', 'should be a month'],
        week: ['Week', 'should be a week'],
        url: ['URL', 'should be a URL'],
        tel: ['Phone Number', 'should be a phone number'],
        color: ['Color', 'should be a color']
    })
    .directive('formField', ["$timeout", "FieldTypes", function ($timeout) {
        return {
            restrict: 'EA',
            templateUrl: '/static/partials/formDirectives/form-fields-dynamic.html',
            replace: true,
            scope: {
                record: '=',
                field: '@',
                type: '@',
                data: '=',
                multiple: '@',
                live: '@',
                required: '@'
            },
            link: function ($scope, element, el, attr) {
                $scope.blurUpdate = function () {
                    if ($scope.live !== 'false') {
                        if ($scope[$scope.field].$valid) {
                            $scope.record.$update(function (updatedRecord) {
                                $scope.record = updatedRecord;
                                $scope.record.$promise.then(function (data) {
                                    $scope.hurray = data;
                                });
                            });
                        } else {
                            console.log("hey hi ya");
                        }
                    } else {
                            console.log("hey hi");
                    }
                };

                var saveTimeout;
                $scope.update = function () {
                    $timeout.cancel(saveTimeout);
                    saveTimeout = $timeout($scope.blurUpdate, 1000);
                };
            }
        };
    }])
    .directive('file', function(){
        return {
            scope: {
                file: '='
            },
            link: function(scope, el, attrs){
                el.bind('change', function(event){
                    var files = event.target.files;
                    var file = files[0];
                    scope.file = file ? file.name : undefined;
                    scope.$apply();
                });
            }
        };
    });
