function Rank() {
    let self = this;
    self.nicknameInput = $("input[name='nickname']");
    self.gameNameInput = $("input[name='game_name']");
    self.hourInput = $("input[name='hour']");
    self.minuteInput = $("input[name='minute']");
    self.secondInput = $("input[name='second']");
    self.millisecondInput = $("input[name='millisecond']");
    self.platformSelect = $("#platform");
    self.pageSkipInput = $("input[name='page-skip']");
    self.saveBtn = $('#save-btn');  // 获取保存按钮
}

Rank.prototype.run = function () {
    let self = this;
    self.listenAddRankEvent();
    self.listenEditRankEvent();
    self.listenDeleteRankEvent();
    self.listenPageSkipEvent();
};

Rank.prototype.listenAddRankEvent = function () {
    let self = this;
    let addBtn = $('#add-btn');
    addBtn.click(function () {
        self.saveBtn.addClass('add-submit').removeClass('edit-submit');  // 动态绑定保存按钮的类
        $("#myModalLabel").text("添加排行");  // 模态框的标题
        $('#myModal').modal();  // 显示模态框
    });
    $(document).on('click', '.add-submit', function () {  //获取动态绑定的按钮的单击事件，需要使用document
        xfzajax.post({
            'url': '/rank/add_rank/',
            'data': {
                'nickname': self.nicknameInput.val(),
                'game_name': self.gameNameInput.val(),
                'duration': self.hourInput.val() + 'h' + self.minuteInput.val() + 'm' + self.secondInput.val() + 's' + self.millisecondInput.val() + 'ms',
                'platform': self.platformSelect.val(),
            },
            'success': function (result) {
                if (result['code'] === 200) {
                    alert('添加成功');
                    window.location.reload();
                }
            },
            'fail': function (error) {
                alert(error);
            }
        });
    });
};

Rank.prototype.listenEditRankEvent = function () {
    let self = this;
    let editBtn = $(".edit-btn");
    let rankInput = $("#rank-pk");
    editBtn.click(function () {
        self.saveBtn.addClass('edit-submit').removeClass('add-submit');
        let currentBtn = $(this);
        let tr = currentBtn.parent().parent();
        let pk = tr.attr('data-pk');  // 需要先绑定一个pk到当前的tr上
        $("#myModalLabel").text("编辑排行");
        $('#myModal').modal();
        self.nicknameInput.val(tr.children('.nickname').text());
        self.gameNameInput.val(tr.children('.game_name').text());
        rankInput.val(pk);  // 将值使用隐式传到后台
    });
    $(document).on('click', '.edit-submit', function () {
        xfzajax.post({
            'url': '/rank/edit_rank/',
            'data': {
                'pk': rankInput.val(),  // 因为编辑需要获取当前的主键，所以也要传过去
                'nickname': self.nicknameInput.val(),
                'game_name': self.gameNameInput.val(),
                'duration': self.hourInput.val() + 'h' + self.minuteInput.val() + 'm' + self.secondInput.val() + 's' + self.millisecondInput.val() + 'ms',
                'platform': self.platformSelect.val(),
            },
            'success': function (result) {
                if (result['code'] === 200) {
                    alert('编辑成功');
                    window.location.reload();
                }
            },
            'fail': function (error) {
                alert(error);
            }
        });
    });
};

Rank.prototype.listenDeleteRankEvent = function () {
    let deleteBtn = $(".delete-btn");
    deleteBtn.click(function () {
        let currentBtn = $(this);
        let messageBox = confirm('确定要删除该排行么？');
        if (messageBox === true) {
            let tr = currentBtn.parent().parent();
            let pk = tr.attr('data-pk');  // 与编辑同理，需要传当前主键
            xfzajax.post({
                'url': '/rank/delete_rank/',
                'data': {
                    'pk': pk
                },
                'success': function (result) {
                    if (result['code'] === 200) {
                        window.location.reload();
                    }
                }
            });
        }
    });
};

Rank.prototype.listenPageSkipEvent = function () {  // 监听跳转页码点击事件
    let self = this;
    let skipBtn = $("#skip-btn");
    skipBtn.click(function () {
        if (self.pageSkipInput.val() === '') {
            self.pageSkipInput.val(1);  // 如果输入框是空值，默认给个1
        }
        let url = window.location.href;  // 获取当前的url
        let sHref = window.location.search;  // 获取最后一个/后边的内容
        let paramList = sHref.split("?")[1];  // 使用?分割，并且获取后边的内容
        if (typeof(paramList) === 'undefined') {  // 如果是undefined，就直接跳转
            window.location.href = url.split("?")[0] + '?p=' + self.pageSkipInput.val();
        } else {
            let args = paramList.split("&");
            let newUrl = url.split('?')[0] + '?';
            for (let i = 0; i < args.length; i++) {
                paramList = args[i];
                let arg = paramList.split("=");
                // if (arg[0] === 'org_name') {
                //     newUrl = newUrl + 'org_name=' + arg[1] + '&';  // org_name，就拼接
                // }
            }
            window.location.href = newUrl + 'p=' + self.pageSkipInput.val();
        }
    });
};

$(function () {
    let rank = new Rank();
    rank.run();
});
