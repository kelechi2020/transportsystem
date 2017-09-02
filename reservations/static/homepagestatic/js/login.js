/**
* Created by KELECHI on 9/2/2017.
*/


            var formAjaxSubmit = function(form, modal) {
                $(form).submit(function (e) {
                    e.preventDefault();
                    $.ajax({
                        type: $(this).attr('method'),
                        url: $(this).attr('action'),
                        data: $(this).serialize(),
                        success: function (xhr, ajaxOptions, thrownError) {
                            if ( $(xhr).find('.has-error').length > 0 ) {
                                $(modal).find('.modal-body').html(xhr);
                                formAjaxSubmit(form, modal);
                            } else {
                                $(modal).modal('toggle');
                            }
                        },
                        error: function (xhr, ajaxOptions, thrownError) {
                        }
                    });
                });
            }
            $('#comment-button').click(function() {
                $('#form-modal-body').load('/new-user/', function () {
                    $('#form-modal').modal('toggle');
                    formAjaxSubmit('#form-modal-body form', '#form-modal');
                });
            });
