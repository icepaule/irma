'use strict';

angular.module('irma')
.directive('fileTrigger', [function() {
  return {
    link: function(scope, element, attr) {
      element.click(function(){
        $('#file-container').click();
      });
    }
  };
}]);

angular.module('irma')
.directive('booleanDisplay', [function() {
  return {
    restrict: 'A',
    scope: {state: '=booleanDisplay', color: '@color'},
    template: '<span class="glyphicon glyphicon-{{(state)? \'ok\': \'remove\'}}" style="color: {{(color)? color: (state)? \'#5cb85c\': \'#d9534f\'}}"></span>'
  };
}]);

angular.module('irma')
.directive('alerts', ['alerts', function(alerts) {
  return {
    restrict: 'E',
    template: '<div class="alerts"><ul class="list-unstyled"><li class="alert-{{alert.type}}" ng-repeat="alert in alerts" ng-bind-html="alert.message"></li></ul></div>',
    link: function(scope, element, attr) {
      scope.alerts = alerts.list();
    }
  };
}]);