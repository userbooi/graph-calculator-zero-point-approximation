from plotly.graph_objs import Layout
from plotly import offline
from x_and_y_points import GetInfo
import math

print('use spaces to separate each number/letter/symbol\n')

info = GetInfo(None, None, [], [])
info.get_user_input()

data = [
    {'type':'scatter',
     'x': info.x_value,
     'y': info.y_value,
     'marker':{
         'color': 'blue'
     },
}]

x_axis_config = {'title': 'x value'}
y_axis_config = {'title': 'y value'}

my_Layout = Layout(title='graph of function y = x^2', xaxis=x_axis_config, yaxis=y_axis_config)

offline.plot({'data': data, 'layout': my_Layout}, filename='graph.html')

answer = input("\nDo you want the zero point approximation (yes, or no)?: ")

if answer.title() == "Yes":
    zero_point_approximation = None
    response = ""
    precision = float(input("\nEnter the amount of precision you want: "))

    for x in info.x_value:
        if info.make_y_value(info.function, float(x)) == 0:
            zero_point_approximation = float(x)

            response += ", " + str(x)
        else:
            if info.x_value.index(x) != len(info.x_value) - 1:
                if info.make_y_value(info.function, float(x)) * info.make_y_value(info.function, float(info.x_value[info.x_value.index(x) + 1])) < 0:
                    x1 = float(x)
                    x2 = float(info.x_value[info.x_value.index(x) + 1])
                    middle_num = 0.0

                    if info.make_y_value(info.function, x1) < 0:
                        while True:
                            if math.fabs(float(x2 - x1)) < precision:
                                zero_point_approximation = x1
                                break
                            else:
                                middle_num = (x1 + x2) / 2

                            if info.make_y_value(info.function, middle_num) > 0:
                                x2 = middle_num
                            elif info.make_y_value(info.function, middle_num) == 0:
                                zero_point_approximation = middle_num
                                break
                            else:
                                x1 = middle_num

                        response += ", " + str(zero_point_approximation)

                    else:
                        while True:
                            if math.fabs(float(x1 - x2)) < precision:
                                zero_point_approximation = x2
                                break
                            else:
                                middle_num = (x2 + x1) / 2

                            if info.make_y_value(info.function, middle_num) > 0:
                                x1 = middle_num
                            elif info.make_y_value(info.function, middle_num) == 0:
                                zero_point_approximation = middle_num
                                break
                            else:
                                x2 = middle_num

                        response += ", " + str(zero_point_approximation)

    print(f"The point(s): {response}")
