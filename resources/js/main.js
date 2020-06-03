// function parent(userID, password, email) {
//   this.userID = userID;
//   this.password = password;
//   this.email = email; 	  

// }

// function child(name, parentUserID) {
//   this.name = name;
//   this.parentUserID = parentUserID;
// }
// this 
// https://requirejs.org/docs/errors.html#notloaded
// https://requirejs.org/docs/errors.html#scripterror
// require.config({
//   paths: {
//       'dependency': 'http://some.domain.dom/path/to/dependency'
//   }
// });

// //DO NOT DO THIS
// require(['http://some.domain.dom/path/to/dependency.js'],
// function (dependency) {});

// //Rather, do this:
// require.config({
//     paths: {
//         'dependency': 'http://some.domain.dom/path/to/dependency'
//     }
// });

// require(['dependency'], function (dependency) {});
//"tui-calendar": "^1.12.13"
// require.config({
//       paths: {
//         "tui-calendar": "^1.12.13"
//       }
//   });
  
// require(['tui-calendar'], function (dependency) {});
  


// /* CommonJS */
// var Calendar =  require(['tui-calendar'], function () {
  
//   require(["tui-calendar/dist/tui-calendar.css"], function () {
//     var calendar = new Calendar('#calendar', {
//       defaultView: 'month',
//       taskView: true,
//       template: {
//         monthDayname: function(dayname) {
//           return '<span class="calendar-week-dayname-name">' + dayname.label + '</span>';
//         }
//       }
//     })
//   });
// });


// If you use the default popups, use this.
// require("tui-date-picker/dist/tui-date-picker.css");
// require("tui-time-picker/dist/tui-time-picker.css");

