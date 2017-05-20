    $(document).ready(function () {
            $("#phone").mask('+7(999)-99-99-999');
            $("#city").change(function () {
            var city = $("#city").val();
            switch (city){
                case "Севастополь":$("#district").empty().prepend(
                                $('<option value="Северная">Северная</option>'),
                                $('<option value="Центр">Центр</option>'),
                                $('<option value="Набережная">Набережная</option>'),
                                $('<option value="Ялтинская">Ялтинская</option>'));
                    break;
                case "Симферополь":$("#district").empty().prepend(
                                $('<option value="Центр">Центр</option>'),
                                $('<option value="Ж/Д">Ж/Д</option>'),
                                $('<option value="Москольцо">Москольцо</option>'),
                                $('<option value="Севастопольскя">Севастопольская</option>'),
                                $('<option value="Марьино">Марьино</option>'),
                                $('<option value="пл.Куйбышева">пл.Куйбышева</option>'));
            }
        })


    });
    /**
 * Created by arif on 19.05.2017.
 */
