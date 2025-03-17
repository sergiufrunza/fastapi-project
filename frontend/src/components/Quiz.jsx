import {useState} from "react";
import {useNavigate} from "react-router-dom";

export function Quiz({data}) {
    const navigate = useNavigate();
    const [selectedAnswer, setSelectedAnswer] = useState(null);
    const [isSubmitted, setIsSubmitted] = useState(false);
    const [currentQuiz, setCurrentQuiz] = useState(1);
    const [correctAnswers, setCorrectAnswers] = useState(0);
    const [endQuiz, setEndQuiz] = useState(false);
    const len_quiz = data.quiz.length;

    const handleSelectAnswer = (index, isCorrect) => {
        setSelectedAnswer({index, isCorrect});
        setIsSubmitted(false);
    };
    const handleSubmit = () => {
        if (!selectedAnswer) return;
        if (selectedAnswer.isCorrect) {
            setCorrectAnswers(correctAnswers + 1)
        }
        setIsSubmitted(true);
    };
    const handleNext = () => {
        if (!selectedAnswer) return;
        if (currentQuiz === len_quiz) {
            setEndQuiz(true)
        }
        setCurrentQuiz(currentQuiz + 1)
        setIsSubmitted(false);
        setSelectedAnswer(null);
    };
    const handleToUpload = () => {
        navigate("/upload")
    };
    const handleToReload = () => {
        window.location.reload();
    };
    if (endQuiz) {
        return (
            <div className="p-7 shadow-md rounded-2xl sm:mx-auto sm:w-full sm:max-w-md flex flex-col gap-4">
                <h2 className="text-center text-2xl font-bold tracking-tight text-gray-900 ">Correct
                    Answers {correctAnswers}/{len_quiz}</h2>
                <div className="flex gap-6 items-center">
                    <button type="button"
                            className="flex w-full justify-center rounded-md px-3 py-1.5 text-sm/6 font-semibold text-white shadow-xs  focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600 bg-blue-600 hover:bg-blue-700 cursor-pointer text-white"
                            onClick={handleToUpload}>
                        Încarcă alt PDF
                    </button>
                    <button type="button"
                            className="flex w-full justify-center rounded-md px-3 py-1.5 text-sm/6 font-semibold text-white shadow-xs  focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600 bg-blue-600 hover:bg-blue-700 cursor-pointer text-white"
                            onClick={handleToReload}>
                        Mai încearcă o dată
                    </button>
                </div>
            </div>
        )
    }
    return (
        <div className="p-7 shadow-md rounded-2xl sm:mx-auto sm:w-full sm:max-w-md flex flex-col gap-4">
            <h2 className="text-center text-2xl font-bold tracking-tight text-gray-900 ">{data.quiz[currentQuiz - 1].q}</h2>
            <div className="text-center text-base font-bold tracking-tight text-gray-600">{currentQuiz}/{len_quiz}</div>

            <div className="flex flex-col gap-4">
                {data && data.quiz[currentQuiz - 1].a.map((answer, index) => {
                    const isSelected = selectedAnswer?.index === index;

                    let bgColor = "bg-gray-200 text-gray-900";
                    if (isSubmitted) {
                        bgColor = answer.s
                            ? "bg-green-500 text-white"
                            : bgColor;
                        if (isSelected) {
                            bgColor = selectedAnswer.isCorrect
                                ? "bg-green-500 text-white"
                                : "bg-red-500 text-white";
                        }
                    } else if (isSelected) {
                        bgColor = "bg-indigo-300 text-white";
                    }
                    return (
                        <div key={index}>
                            <input
                                type="checkbox"
                                id={`answer-${index}`}
                                className="hidden"
                                checked={selectedAnswer?.index === index}

                                onChange={() => {
                                }}
                            />
                            <label
                                htmlFor={`answer-${index}`}
                                className={`block w-full px-3 py-1.5 rounded-md  text-sm/6 cursor-pointer transition-colors duration-300 ${bgColor}`}
                                onClick={() => isSubmitted ? null : handleSelectAnswer(index, answer.s)}
                            >
                                {answer.v}
                            </label>

                        </div>
                    );
                })}
                <button type="button"
                        className={`flex w-full justify-center rounded-md px-3 py-1.5 text-sm/6 font-semibold text-white shadow-xs  focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600
                                        ${
                            selectedAnswer
                                ? 'bg-blue-600 hover:bg-blue-700 cursor-pointer text-white'
                                : 'bg-gray-400 cursor-not-allowed text-gray-700'
                        }`}
                        onClick={isSubmitted ? handleNext : handleSubmit}
                        disabled={!selectedAnswer}>
                    {isSubmitted ? "Următorul" : "Verifică răspunsul"}

                </button>
            </div>
        </div>
    );
}